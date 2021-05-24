using System;
using System.Diagnostics;
using System.IO;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;

namespace Almostengr.TrafficPi.Web.Controllers
{
    public abstract class ControllerBase : Controller
    {
        private readonly ILogger<ControllerBase> _logger;
        private readonly AppSettings _appSettings;

        public ControllerBase(ILogger<ControllerBase> logger, AppSettings appSettings)
        {
            _logger = logger;
            _appSettings = appSettings;
        }
        
        public bool StopWorkerProcess()
        {
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

                foreach (var singleLine in output.Split("\n"))
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
            }
            catch (Exception ex)
            {
                _logger.LogError(ex.Message);
            }

            return shutdownSuccess;
        }

        public void StartWorkerProcess(string programName)
        {
            try
            {
                _logger.LogInformation("Starting new process");

                Process process = new Process()
                {
                    StartInfo = new ProcessStartInfo()
                    {
                        FileName = _appSettings.LampControlPath,
                        Arguments = $"--{programName} > /dev/null 2>&1 &",
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
        }

        public void ShutDownSystem()
        {
            Process process = new Process()
            {
                StartInfo = new ProcessStartInfo()
                {
                    FileName = "shutdown",
                    ArgumentList = {
                        "-h",
                        "now"
                    },
                    RedirectStandardError = true,
                    RedirectStandardOutput = true,
                    UseShellExecute = false,
                    CreateNoWindow = true,
                }
            };

            process.Start();
        }

        public void RebootSystem()
        {
            Process process = new Process()
            {
                StartInfo = new ProcessStartInfo()
                {
                    FileName = "reboot",
                    RedirectStandardError = true,
                    RedirectStandardOutput = true,
                    UseShellExecute = false,
                    CreateNoWindow = true,
                }
            };

            process.Start();
        }
    }
}