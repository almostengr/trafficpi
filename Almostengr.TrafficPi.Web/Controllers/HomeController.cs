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
        private readonly AppSettings _appSettings;

        public HomeController(ILogger<HomeController> logger, AppSettings appSettings) : base(logger, appSettings)
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

            _logger.LogInformation("Shutting down previous process");

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

            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }

    }
}
