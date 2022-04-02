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
            while (!stoppingToken.IsCancellationRequested)
            {
                _signalIndication.GreenLight();
                await Task.Delay(TimeSpan.FromSeconds(RedGreenDelay()), stoppingToken);

                _signalIndication.YellowLight();
                await Task.Delay(TimeSpan.FromSeconds(YellowDelay()), stoppingToken);

                _signalIndication.RedLight();
                await Task.Delay(TimeSpan.FromSeconds(RedGreenDelay()), stoppingToken);
            }
        }
    }
}