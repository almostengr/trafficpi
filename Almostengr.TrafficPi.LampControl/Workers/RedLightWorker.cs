using System;
using System.Threading;
using System.Threading.Tasks;
using Almostengr.TrafficPi.LampControl.Common;
using Almostengr.TrafficPi.LampControl.Services;
using Microsoft.Extensions.Logging;

namespace Almostengr.TrafficPi.LampControl.Workers
{
    public class RedLightWorker : BaseWorker
    {
        public RedLightWorker(ILogger<BaseWorker> logger, ISignalIndicationService signalIndication) : 
            base(logger, signalIndication)
        {
        }

        protected override async Task ExecuteAsync(CancellationToken stoppingToken)
        {
            while (!stoppingToken.IsCancellationRequested)
            {
                _signalIndication.RedLight();
                await Task.Delay(TimeSpan.FromMinutes(DelaySeconds.Maximum), stoppingToken);
            }
        }
    }
}