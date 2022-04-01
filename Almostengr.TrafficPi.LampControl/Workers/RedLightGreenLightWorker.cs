using System;
using System.Threading;
using System.Threading.Tasks;
using Almostengr.TrafficPi.LampControl.Services;
using Microsoft.Extensions.Logging;

namespace Almostengr.TrafficPi.LampControl.Workers
{
    public class RedLightGreenLightWorker : BaseWorker
    {
        public RedLightGreenLightWorker(ILogger<BaseWorker> logger, ISignalIndicationService signalIndication) : 
            base(logger, signalIndication)
        {
        }

        protected override async Task ExecuteAsync(CancellationToken stoppingToken)
        {
            while (!stoppingToken.IsCancellationRequested)
            {
                _signalIndication.RedLight();
                await Task.Delay(TimeSpan.FromSeconds(random.Next(2, 10)), stoppingToken);

                _signalIndication.GreenLight();
                await Task.Delay(TimeSpan.FromSeconds(random.Next(1, 4)), stoppingToken);
            }
        }
    }
}