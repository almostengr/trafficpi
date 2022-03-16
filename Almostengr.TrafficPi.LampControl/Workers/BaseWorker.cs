using System;
using System.Threading;
using System.Threading.Tasks;
using Almostengr.TrafficPi.LampControl.Services;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;

namespace Almostengr.TrafficPi.LampControl.Workers
{
    public abstract class BaseWorker : BackgroundService
    {
        internal readonly ILogger<BaseWorker> _logger;
        // internal readonly GpioService _gpio;
        internal readonly ISignalIndicationService _signalIndication;
        internal Random random = new Random();
        // internal PinValue LampOff = PinValue.High;
        // internal PinValue LampOn = PinValue.Low;
        internal const int FlasherDelay = 700;
        // private const int RedLightPin = 11;
        // private const int YellowLightPin = 9;
        // private const int GreenLightPin = 10;

        public BaseWorker(ILogger<BaseWorker> logger, ISignalIndicationService signalIndication)
        {
            _logger = logger;
            _signalIndication = signalIndication;


            // _gpio.OpenOutputPin(RedLightPin);
            // _gpio.OpenOutputPin(YellowLightPin);
            // _gpio.OpenOutputPin(GreenLightPin);
        }

        protected override async Task ExecuteAsync(CancellationToken stoppingToken)
        {
            throw new NotImplementedException();
        }

        // internal void ChangeSignal(PinValue redLight, PinValue yellowLight, PinValue greenLight)
        // {
        // }

        // internal void ShutdownGpio(GpioController gpio)
        // {
        //     _logger.LogInformation("Shutting down traffic controller");

        //     _gpio.TurnOffGpio(RedLightPin);
        //     _gpio.TurnOffGpio(YellowLightPin);
        //     _gpio.TurnOffGpio(GreenLightPin);            

        //     _gpio.CloseOutputPin(RedLightPin);
        //     _gpio.CloseOutputPin(YellowLightPin);
        //     _gpio.CloseOutputPin(GreenLightPin);
        // }

        // internal void InitializeGpio(GpioController gpio)
        // {
        //     _logger.LogInformation("Initializing traffic controller");

        //     _gpio.OpenOutputPin(RedLightPin);
        //     _gpio.OpenOutputPin(YellowLightPin);
        //     _gpio.OpenOutputPin(GreenLightPin);
        // }

        internal int YellowDelay()
        {
            return random.Next(1, 5);
        }

        internal virtual int RedGreenDelay()
        {
            return random.Next(5, 60);
        }

        public override Task StartAsync(CancellationToken cancellationToken)
        {
            _logger.LogInformation("Initializing traffic controller");
            
            _signalIndication.InitializeLights();
            return base.StartAsync(cancellationToken);
        }

        public override Task StopAsync(CancellationToken cancellationToken)
        {
            _signalIndication.ShutdownLights();
            return base.StopAsync(cancellationToken);
        }

        public override void Dispose()
        {
            _logger.LogInformation("Shutting down traffic controller");
            
            _signalIndication.ShutdownLights();

            base.Dispose();
        }
    }
}