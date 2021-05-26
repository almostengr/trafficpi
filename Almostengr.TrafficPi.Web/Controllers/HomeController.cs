using System;
using System.Diagnostics;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Almostengr.TrafficPi.Web.Models;
using Microsoft.AspNetCore.Http;

namespace Almostengr.TrafficPi.Web.Controllers
{
    public class HomeController : ControllerBase
    {
        private readonly ILogger<HomeController> _logger;

        public HomeController(ILogger<HomeController> logger) : base(logger)
        {
            _logger = logger;
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

            bool shutdownSuccess = StopWorkerProcess();

            if (trafficProgram.Program == "shutdown")
            {
                ShutDownSystem();
            }
            else if (trafficProgram.Program == "restart")
            {
                RebootSystem();
            }
            else if (shutdownSuccess == false)
            {
                _logger.LogError("Previous program did not shutdown"); // don't start program
            }
            else
            {
                StartWorkerProcess(trafficProgram.Program);
            }

            return View(trafficProgram);
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }

    }
}
