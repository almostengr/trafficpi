using System;
using System.Diagnostics;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Almostengr.TrafficPi.Web.Models;
using Microsoft.AspNetCore.Http;
using System.IO;

namespace Almostengr.TrafficPi.Web.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;
        private readonly AppSettings _appSettings;

        public HomeController(ILogger<HomeController> logger,
            AppSettings appSettings)
        {
            _logger = logger;
            _appSettings = appSettings;
        }

        [HttpGet]
        public IActionResult Index()
        {
            return View();
        }

        [HttpPost]
        public IActionResult Index(TrafficProgram trafficProgram)
        {
            if (trafficProgram == null)
                throw new ArgumentNullException();

            Process process;
            bool shutdownSuccess = false;

            try
            {
                _logger.LogInformation("Shutting down previous process");

                process = new Process()
                {
                    StartInfo = new ProcessStartInfo()
                    {
                        FileName = "pgrep",
                        ArgumentList = {
                            "-f",
                            "Almostengr.TrafficPi.LampControl"
                            },
                        RedirectStandardError = true,
                        RedirectStandardOutput = true,
                        UseShellExecute = false,
                        CreateNoWindow = true,
                    }
                };

                process.Start();
                process.WaitForExit();

                StreamReader streamReaderOut = process.StandardOutput;
                string output = streamReaderOut.ReadToEnd();
                _logger.LogInformation(streamReaderOut.ReadToEnd());

                output = output.Trim();

                foreach(var singleLine in output.Split("\n"))
                {
                    
                    process = new Process()
                    {
                        StartInfo = new ProcessStartInfo()
                        {
                            FileName = "/bin/kill",
                            Arguments = singleLine,
                            RedirectStandardError = true,
                            RedirectStandardOutput = true,
                            UseShellExecute = false,
                            CreateNoWindow = true,
                        }
                    };

                    _logger.LogInformation("terminating PID " + singleLine);

                    process.Start();
                    process.WaitForExit();

                    shutdownSuccess = true;
                }

                _logger.LogInformation("Done shutting down previous process");
                shutdownSuccess = true;
            }
            catch (Exception ex)
            {
                _logger.LogError(ex.Message);
            }

            if (trafficProgram.Program == "shutdown" || 
                trafficProgram.Program == "restart" || 
                shutdownSuccess == false)
            {
                goto Return;
            }

            try
            {
                _logger.LogInformation("Starting new process");

                process = new Process()
                {
                    StartInfo = new ProcessStartInfo()
                    {
                        FileName = _appSettings.LampControlPath,
                        Arguments = $"--{trafficProgram.Program} > /dev/null 2>&1 &",
                        RedirectStandardError = true,
                        RedirectStandardOutput = true,
                        UseShellExecute = false,
                        CreateNoWindow = true,
                    }
                };

                process.Start();

                _logger.LogInformation("Done starting new process");
            }
            catch (Exception ex)
            {
                _logger.LogError(ex.Message);
            }

        Return:
            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }

    }
}
