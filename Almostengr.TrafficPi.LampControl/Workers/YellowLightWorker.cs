using System;
using System.Threading;
using System.Threading.Tasks;
using Almostengr.TrafficPi.LampControl.Common;
using Almostengr.TrafficPi.LampControl.Services;
using Microsoft.Extensions.Logging;

namespace Almostengr.TrafficPi.LampControl.Workers
{
    public class YellowLightWorker : BaseWorker
    {
        public YellowLightWorker(ILogger<YellowLightWorker> logger, ISignalIndicationService signalIndication) : 
            base(logger, signalIndication)
        {
        }

        protected override async Task ExecuteAsync(CancellationToken stoppingToken)
        {
            while (!stoppingToken.IsCancellationRequested)
            {
                _signalIndication.YellowLight();
                await Task.Delay(TimeSpan.FromMinutes(DelaySeconds.Maximum), stoppingToken);
            }
        }
    }
}