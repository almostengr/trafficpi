using System;
using System.Threading;
using System.Threading.Tasks;
using Almostengr.TrafficPi.LampControl.Services;
using Microsoft.Extensions.Logging;

namespace Almostengr.TrafficPi.LampControl.Workers
{
    public class Tm2To3Worker : BaseWorker
    {
        public Tm2To3Worker(ILogger<BaseWorker> logger, ISignalIndicationService signalIndication) : 
            base(logger, signalIndication)
        {
        }

        protected override async Task ExecuteAsync(CancellationToken stoppingToken)
        {
            while (!stoppingToken.IsCancellationRequested)
            {
                _signalIndication.AllLights();
                await Task.Delay(TimeSpan.FromSeconds(1), stoppingToken);

                _signalIndication.NoLights();
                await Task.Delay(TimeSpan.FromMinutes(2), stoppingToken);

                _signalIndication.GreenLight();
                await Task.Delay(TimeSpan.FromSeconds(30), stoppingToken);

                _signalIndication.YellowLight();
                await Task.Delay(TimeSpan.FromSeconds(30), stoppingToken);

                _signalIndication.RedLight();
                await Task.Delay(TimeSpan.FromHours(1), stoppingToken);
            }
        }

    }
}