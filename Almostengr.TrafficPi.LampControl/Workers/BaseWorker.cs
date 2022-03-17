using System;
using System.Threading;
using System.Threading.Tasks;
using Almostengr.TrafficPi.LampControl.Services;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;

namespace Almostengr.TrafficPi.LampControl.Workers
{
    public abstract class BaseWorker : BackgroundService
    {
        internal readonly ILogger<BaseWorker> _logger;
        internal readonly ISignalIndicationService _signalIndication;
        internal Random random = new Random();
        internal const int FlasherDelay = 700;

        public BaseWorker(ILogger<BaseWorker> logger, ISignalIndicationService signalIndication)
        {
            _logger = logger;
            _signalIndication = signalIndication;
        }

        protected override Task ExecuteAsync(CancellationToken stoppingToken)
        {
            throw new NotImplementedException();
        }

        internal int YellowDelay()
        {
            return random.Next(1, 5);
        }

        internal virtual int RedGreenDelay()
        {
            return random.Next(5, 60);
        }

        public override Task StartAsync(CancellationToken cancellationToken)
        {
            _logger.LogInformation("Initializing traffic controller");
            
            _signalIndication.InitializeLights();
            return base.StartAsync(cancellationToken);
        }

        public override Task StopAsync(CancellationToken cancellationToken)
        {
            _signalIndication.ShutdownLights();
            return base.StopAsync(cancellationToken);
        }

        public override void Dispose()
        {
            _logger.LogInformation("Shutting down traffic controller");
            
            _signalIndication.ShutdownLights();

            base.Dispose();
        }
    }
}