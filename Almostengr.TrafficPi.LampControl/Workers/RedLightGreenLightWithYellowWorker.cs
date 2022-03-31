using System;
using System.Threading;
using System.Threading.Tasks;
using Almostengr.TrafficPi.LampControl.Services;
using Microsoft.Extensions.Logging;

namespace Almostengr.TrafficPi.LampControl.Workers
{
    public class RedLightGreenLightWithYellowWorker : BaseWorker
    {
        public RedLightGreenLightWithYellowWorker(ILogger<BaseWorker> logger, ISignalIndicationService signalIndication) : 
            base(logger, signalIndication)
        {
        }
        
        protected override async Task ExecuteAsync(CancellationToken stoppingToken)
        {
            int wait;

            while (!stoppingToken.IsCancellationRequested)
            {
                _signalIndication.RedLight();
                wait = random.Next(2, 10);
                await Task.Delay(TimeSpan.FromSeconds(wait), stoppingToken);

                _signalIndication.GreenLight();
                wait = random.Next(1, 3);
                await Task.Delay(TimeSpan.FromSeconds(wait), stoppingToken);

                _signalIndication.YellowLight();
                wait = random.Next(1, 4);
                await Task.Delay(TimeSpan.FromSeconds(wait), stoppingToken);
            }
        }
    }
}