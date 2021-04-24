using System;
using System.Diagnostics;
using Almostengr.TrafficPi.Api.Models;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;

namespace Almostengr.TrafficPi.Api.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class TrafficController : ControllerBase
    {
        public readonly ILogger<TrafficController> _logger;
        public readonly AppSettings _appSettings;

        // public TrafficController(ILogger<TrafficController> logger, AppSettings appSettings)
        public TrafficController(ILogger<TrafficController> logger)
        {
            _logger = logger;
            // _appSettings = appSettings;
        }

        [HttpPost]
        [ProducesResponseType(StatusCodes.Status201Created)]
        [ProducesResponseType(StatusCodes.Status400BadRequest)]
        public IActionResult Post(string id)
        {
            if (id == null)
                throw new ArgumentNullException();

            Process process;

            try
            {
                _logger.LogInformation("Shutting down previous process");

                process = new Process()
                {
                    StartInfo = new ProcessStartInfo()
                    {
                        FileName = "/bin/kill",
                        Arguments = "$(ps -ef | grep Almostengr.TrafficPi.LampControl | awk '{print $2}')",
                        RedirectStandardError = true,
                        RedirectStandardOutput = true,
                        UseShellExecute = false,
                        CreateNoWindow = true,
                    }
                };

                process.Start();

                process.WaitForExit();

                _logger.LogInformation("Done shutting down previous process");

                // string output = process.StandardOutput.ReadToEnd();

                // if (string.IsNullOrEmpty(output) == false)
                // {

                // }
            }
            catch (Exception ex)
            {
                _logger.LogError(ex.Message);
            }

            try
            {
                _logger.LogInformation("Starting new process");

                process = new Process()
                {
                    StartInfo = new ProcessStartInfo()
                    {
                        FileName = _appSettings.LampControlPath,
                        Arguments = $"--{id} > /dev/null 2>&1 &",
                        RedirectStandardError = true,
                        RedirectStandardOutput = true,
                        UseShellExecute = false,
                        CreateNoWindow = true,
                    }
                };

                process.Start();

                _logger.LogInformation("Done starting new process");

                return Ok();
            }
            catch (Exception ex)
            {
                _logger.LogError(ex.Message);

                return BadRequest();
            }
        }

        [HttpGet]
        [Route("health")]
        [ProducesResponseType(StatusCodes.Status200OK)]
        public IActionResult Health()
        {
            return Ok();
        }

        [HttpGet]
        [ProducesResponseType(StatusCodes.Status200OK)]
        public IActionResult Index()
        {
            return Ok();
        }

        private IActionResult TerminateProcess()
        {
            try
            {
                Process process = new Process()
                {
                    StartInfo = new ProcessStartInfo()
                    {
                        FileName = "/bin/ps",
                        Arguments = "",
                        RedirectStandardError = true,
                        RedirectStandardOutput = true,
                        UseShellExecute = false,
                        CreateNoWindow = true,
                    }
                };

                process.Start();

                SignalProgram signalProgram = new SignalProgram(process);

                return Ok();
            }
            catch (Exception ex)
            {
                _logger.LogError(ex.Message);

                return BadRequest();
            }
        }

    }
}