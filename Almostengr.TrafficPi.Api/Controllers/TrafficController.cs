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
        public readonly TrafficSignalDbContext _context;

        // public TrafficController(ILogger<TrafficController> logger, AppSettings appSettings)
        public TrafficController(ILogger<TrafficController> logger, TrafficSignalDbContext context)
        {
            _logger = logger;
            _context = context;
            // _appSettings = appSettings;
        }

        [HttpPost]
        [ProducesResponseType(StatusCodes.Status201Created)]
        [ProducesResponseType(StatusCodes.Status400BadRequest)]
        public IActionResult Post(string id)
        {
            if (id == null)
                throw new ArgumentNullException();

            try
            {

                Process process = new Process()
                {
                    StartInfo = new ProcessStartInfo()
                    {
                        FileName = "",
                        Arguments = "",
                        RedirectStandardError = true,
                        RedirectStandardOutput = true,
                        UseShellExecute = false,
                        CreateNoWindow = true,
                    }
                };

                process.Start();

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