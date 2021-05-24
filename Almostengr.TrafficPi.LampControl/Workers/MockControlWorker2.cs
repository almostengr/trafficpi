using System;
using System.Threading;
using System.Threading.Tasks;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;

namespace Almostengr.TrafficPi.LampControl.Workers
{
    public class MockControlWorker2 : BackgroundService
    {
        private readonly ILogger<MockControlWorker2> _logger;

        public MockControlWorker2(ILogger<MockControlWorker2> logger, AppSettings appSettings)
        {
            _logger = logger;
        }

        public override Task StartAsync(CancellationToken cancellationToken)
        {
            return base.StartAsync(cancellationToken);
        }

        public override Task StopAsync(CancellationToken cancellationToken)
        {
            return base.StopAsync(cancellationToken);
        }

        protected override async Task ExecuteAsync(CancellationToken stoppingToken)
        {
            while(!stoppingToken.IsCancellationRequested)
            {
                _logger.LogInformation("Mock worker 2 is working");
                await Task.Delay(TimeSpan.FromSeconds(1));
            }
        }
    }
}