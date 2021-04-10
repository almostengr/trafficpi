using System;
using System.Threading;
using System.Threading.Tasks;
using Almostengr.TrafficPi.Signal.Enumerables;
using Microsoft.Extensions.Logging;

namespace Almostengr.TrafficPi.LampControl.Workers
{
    public class ManualControlWorker : BaseWorker
    {
        private readonly ILogger<ManualControlWorker> _logger;

        public ManualControlWorker(ILogger<ManualControlWorker> logger)
        {
            _logger = logger;
        }
        
        protected override async Task ExecuteAsync(CancellationToken stoppingToken)
        {
            string input = string.Empty;

            while (input.ToLower() != "q")
            {
                Console.WriteLine("==== Main Menu ====");
                Console.WriteLine();
                Console.WriteLine("0 - All Off");
                Console.WriteLine("1 - Red");
                Console.WriteLine("2 - Yellow");
                Console.WriteLine("3 - Green");
                Console.WriteLine();

                input = Console.ReadLine();

                switch(input)
                {
                    case "0":
                        ChangeSignal(LampState.Off, LampState.Off, LampState.Off);
                        break;

                    case "1":
                        ChangeSignal(LampState.On, LampState.Off, LampState.Off);
                        break;

                    case "2":
                        ChangeSignal(LampState.Off, LampState.On, LampState.Off);
                        break;

                    case "3":
                        ChangeSignal(LampState.Off, LampState.Off, LampState.On);
                        break;

                    case "q":
                        _logger.LogInformation("Exiting...");
                        break;

                    default:
                        break;
                }
            } // end while
        }
    }
}