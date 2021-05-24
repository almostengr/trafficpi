using System;
using System.Device.Gpio;
using Almostengr.TrafficPi.LampControl.Workers;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

namespace Almostengr.TrafficPi.LampControl
{
    public class Program
    {
        public static void Main(string[] args)
        {
            CreateHostBuilder(args).Build().Run();
        }

        public static IHostBuilder CreateHostBuilder(string[] args) =>
            Host.CreateDefaultBuilder(args)
                .ConfigureServices((hostContext, services) =>
                {
                    IConfiguration configuration = hostContext.Configuration;
                    AppSettings appSettings = configuration.GetSection(nameof(AppSettings)).Get<AppSettings>();
                    services.AddSingleton(appSettings);

                    services.AddSingleton<GpioController>();

                    switch (args[0])
                    {
                        case "--mock":
                            services.AddHostedService<MockWorker>();
                            break;

                        case "--mock2":
                            services.AddHostedService<MockWorker2>();
                            break;
                            
                        case "--manual":
                            services.AddHostedService<ManualWorker>();
                            break;

                        case "--us":
                            services.AddHostedService<UsTrafficWorker>();
                            break;

                        case "--uk":
                            services.AddHostedService<UkTrafficWorker>();
                            break;

                        case "--rglight":
                            services.AddHostedService<RedLightGreenLightWorker>();
                            break;

                        case "--rglightyellow":
                            services.AddHostedService<RedLightGreenLightWithYellowWorker>();
                            break;

                        case "--flashred":
                            services.AddHostedService<FlashRedWorker>();
                            break;

                        case "--flashyellow":
                            services.AddHostedService<FlashYellowWorker>();
                            break;

                        case "--flashgreen":
                            services.AddHostedService<FlashGreenWorker>();
                            break;

                        case "--partymode":
                            services.AddHostedService<PartyModeWorker>();
                            break;

                        default:
                            ShowHelp();
                            break;
                    }
                });

        public static void ShowHelp()
        {
            Console.WriteLine("--manual - Manually control each signal via command line");
            Console.WriteLine("--us - Run the signal using the US signal pattern");
            Console.WriteLine("--uk - Run the signal using the UK signal panttern");
            Console.WriteLine("--rglight - Run red light, green light");
            Console.WriteLine("--rglightyeloow - Run red light, green light with yellow");
            Console.WriteLine("--flashred - Flash red signal");
            Console.WriteLine("--flashyellow - Flash yellow signal");
            Console.WriteLine("--flashgreen - Flash green signal");
            Console.WriteLine("--partymode - Randomly flash a signal color(s)");
        }

    }
}
