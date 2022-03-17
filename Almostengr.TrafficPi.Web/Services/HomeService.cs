using System;
using System.Diagnostics;
using System.IO;
using Microsoft.Extensions.Logging;

namespace Almostengr.TrafficPi.Web.Services
{
    public class HomeService : IHomeService 
    {
        private readonly ILogger<HomeService> _logger;

        public HomeService(ILogger<HomeService> logger)
        {
            _logger = logger;
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
                _logger.LogError(ex, ex.Message);
            }

            return shutdownSuccess;
        }

        public void StartWorkerProcess(string programName)
        {
            try
            {
                _logger.LogInformation("Starting new process");

                string LampControlPath = string.Empty;

#if RELEASE
                LampControlPath = "/home/pi/trafficpi/Almostengr.TrafficPi.LampControl";
#else
                LampControlPath = "/home/almostengineer/trafficpi/Almostengr.TrafficPi.LampControl/bin/Debug/net5.0/Almostengr.TrafficPi.LampControl";
#endif

                _logger.LogInformation(string.Concat("Process: ", LampControlPath, " --", programName));

                Process process = new Process()
                {
                    StartInfo = new ProcessStartInfo()
                    {
                        FileName = LampControlPath,
                        ArgumentList = {
                            string.Concat("--", programName),
                        },
                        UseShellExecute = true,
                        CreateNoWindow = true,
                    }
                };

                process.Start();

                _logger.LogInformation("Done starting new process");
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, ex.Message);
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
                    UseShellExecute = true,
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
                    UseShellExecute = true,
                    CreateNoWindow = true,
                }
            };

            process.Start();
        }
    }
}
