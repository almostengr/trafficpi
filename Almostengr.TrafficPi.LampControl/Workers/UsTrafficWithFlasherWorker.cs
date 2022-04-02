using System;
using System.Threading;
using System.Threading.Tasks;
using Almostengr.TrafficPi.LampControl.Services;
using Microsoft.Extensions.Logging;

namespace Almostengr.TrafficPi.LampControl.Workers
{
    public class UsTrafficWithFlasherWorker : BaseWorker
    {
        public UsTrafficWithFlasherWorker(ILogger<BaseWorker> logger, ISignalIndicationService signalIndication) :
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

                bool flashRed = random.Next(0, 5) >= 2 ? true : false;
                int timesToFlash = random.Next(1, 30);

                for (int i = 0; i <= timesToFlash; i++)
                {
                    if (flashRed)
                    {
                        _signalIndication.RedLight();
                    }
                    else
                    {
                        _signalIndication.YellowLight();
                    }
                    await Task.Delay(TimeSpan.FromMilliseconds(FlasherDelay), stoppingToken);

                    _signalIndication.NoLights();
                    await Task.Delay(TimeSpan.FromMilliseconds(FlasherDelay), stoppingToken);
                } // end for
            } // end while
        } // end ExecuteAsync

    }
}