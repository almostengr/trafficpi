using System;
using System.Threading;
using System.Threading.Tasks;
using Almostengr.TrafficPi.LampControl.Services;
using Microsoft.Extensions.Logging;

namespace Almostengr.TrafficPi.LampControl.Workers
{
    public class PartyModeWorker : BaseWorker
    {
        public PartyModeWorker(ILogger<BaseWorker> logger, ISignalIndicationService signalIndication) : 
            base(logger, signalIndication)
        {
        }

        protected override async Task ExecuteAsync(CancellationToken stoppingToken)
        {
            while (!stoppingToken.IsCancellationRequested)
            {
                int phase = random.Next(1, 7);

                switch (phase)
                {
                    case 1:
                        _signalIndication.RedLight();
                        break;

                    case 2:
                        _signalIndication.YellowLight();
                        break;

                    case 3:
                        _signalIndication.GreenLight();
                        break;

                    case 4:
                        _signalIndication.RedYellowLights();
                        break;

                    case 5:
                        _signalIndication.YellowGreenLights();
                        break;

                    case 6:
                        _signalIndication.AllLights();
                        break;
                    
                    case 7:
                        _signalIndication.RedGreenLights();
                        break;

                    default:
                        _signalIndication.NoLights();
                        break;
                }

                await Task.Delay(TimeSpan.FromSeconds(1), stoppingToken);
            }
        }

    }
}