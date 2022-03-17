using System;
using System.Threading;
using System.Threading.Tasks;
using Almostengr.TrafficPi.LampControl.Services;
using Microsoft.Extensions.Logging;

namespace Almostengr.TrafficPi.LampControl.Workers
{
    public class Tm5To7Worker : BaseWorker
    {
        public Tm5To7Worker(ILogger<BaseWorker> logger, ISignalIndicationService signalIndication) : base(logger, signalIndication)
        {
        }

        protected override async Task ExecuteAsync(CancellationToken stoppingToken)
        {
            while (!stoppingToken.IsCancellationRequested)
            {
                _signalIndication.AllLights();
                await Task.Delay(TimeSpan.FromSeconds(1), stoppingToken);

                _signalIndication.NoLights();
                await Task.Delay(TimeSpan.FromMinutes(5), stoppingToken);

                _signalIndication.GreenLight();
                await Task.Delay(TimeSpan.FromSeconds(60), stoppingToken);

                _signalIndication.YellowLight();
                await Task.Delay(TimeSpan.FromSeconds(60), stoppingToken);

                _signalIndication.RedLight();
                await Task.Delay(TimeSpan.FromHours(1), stoppingToken);
            }
        }

    }
}