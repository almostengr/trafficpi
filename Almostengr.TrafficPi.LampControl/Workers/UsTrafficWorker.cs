using System;
using System.Threading;
using System.Threading.Tasks;
using Almostengr.TrafficPi.LampControl.Services;
using Microsoft.Extensions.Logging;

namespace Almostengr.TrafficPi.LampControl.Workers
{
    public class UsTrafficWorker : BaseWorker
    {
        public UsTrafficWorker(ILogger<BaseWorker> logger, ISignalIndicationService signalIndication) : 
            base(logger, signalIndication)
        {
        }

        protected override async Task ExecuteAsync(CancellationToken stoppingToken)
        {
            int wait;

            while (!stoppingToken.IsCancellationRequested)
            {
                _signalIndication.GreenLight();
                wait = RedGreenDelay();
                await Task.Delay(TimeSpan.FromSeconds(wait), stoppingToken);

                _signalIndication.YellowLight();
                wait = YellowDelay();
                await Task.Delay(TimeSpan.FromSeconds(wait), stoppingToken);

                _signalIndication.RedLight();
                wait = RedGreenDelay();
                await Task.Delay(TimeSpan.FromSeconds(wait), stoppingToken);
            }
        }
    }
}