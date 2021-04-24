using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Almostengr.TrafficPi.Web.Models;
using Microsoft.AspNetCore.Http;
using System.Net.Http;

namespace Almostengr.TrafficPi.Web.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;
        private readonly HttpClient _httpClient;
        private readonly AppSettings _appSettings;

        public HomeController(ILogger<HomeController> logger,
            HttpClient httpClient, 
            AppSettings appSettings)
        {
            _logger = logger;
            _httpClient = httpClient;
            _appSettings = appSettings;
        }

        public IActionResult Index()
        {
            return View();
        }

        // public IActionResult Privacy()
        // {
        //     return View();
        // }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }

        [HttpPost]
        public IActionResult Traffic()
        {
            return View();
        }

        [HttpGet]
        public async Task<IActionResult> TrafficAsync()
        {
            _httpClient.BaseAddress = new Uri(_appSettings.ApiUrl);

            HttpResponseMessage response = await _httpClient.PostAsync("traffic");

            return View();
        }
    }
}
