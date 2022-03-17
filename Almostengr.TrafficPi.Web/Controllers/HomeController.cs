using System;
using System.Diagnostics;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Almostengr.TrafficPi.Web.Models;
using Microsoft.AspNetCore.Http;
using Almostengr.TrafficPi.Web.Services;
using Almostengr.TrafficPi.Web.Constants;

namespace Almostengr.TrafficPi.Web.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;
        private readonly IHomeService _homeService;

        public HomeController(ILogger<HomeController> logger, IHomeService homeService)
        {
            _logger = logger;
            _homeService = homeService;
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

            bool shutdownSuccess = _homeService.StopWorkerProcess();

            if (shutdownSuccess == false)
            {
                _logger.LogError("Previous program did not shutdown"); // don't start program
            }
            else if (trafficProgram.Program == ProgramName.ShutDown)
            {
                _homeService.ShutDownSystem();
            }
            else if (trafficProgram.Program == ProgramName.Reboot)
            {
                _homeService.RebootSystem();
            }
            else
            {
                _homeService.StartWorkerProcess(trafficProgram.Program);
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
