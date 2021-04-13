using System;
using System.Device.Gpio;
using System.Threading;

namespace Almostengr.TrafficPi
{
    public class ManualControl : ITrafficControl
    {
        private const int red = 11, yellow = 9, green = 10;
        private PinValue LampOn = PinValue.Low;
        private PinValue LampOff = PinValue.High;
        // private PinValue LampOff = PinValue.Low;
        // private PinValue LampOn = PinValue.High;

        public int GetDelay(int color)
        {
            Random random = new Random();
            int min, max;

            switch (color)
            {
                case 11:
                case 10:
                    min = 5;
                    max = 60;
                    break;
                case 9:
                    min = 2;
                    max = 5;
                    break;
                default:
                    min = 5;
                    max = 10;
                    break;
            }

            return random.Next(min, max) * 1000;
        }

        public void TurnOff(GpioController controller)
        {
            controller.Write(green, LampOff);
            controller.Write(yellow, LampOff);
            controller.Write(red, LampOff);
        }

        public void RunControl()
        {
            Console.WriteLine("Traffic light starting...");

            using GpioController controller = new GpioController();

            controller.OpenPin(green, PinMode.Output);
            controller.OpenPin(yellow, PinMode.Output);
            controller.OpenPin(red, PinMode.Output);

            Console.CancelKeyPress += (s, e) =>
            {
                Console.WriteLine("Shutting down");
                TurnOff(controller);
            };

            TurnOff(controller);

            while (true)
            {
                // controller.Write(green, LampOn);
                // Console.WriteLine("green");

                // Thread.Sleep(GetDelay(green));

                // controller.Write(green, LampOff);
                // controller.Write(yellow, LampOn);
                // Console.WriteLine("yellow");

                // Thread.Sleep(GetDelay(yellow));

                // controller.Write(yellow, LampOff);
                // controller.Write(red, LampOn);
                // Console.WriteLine("red");

                // Thread.Sleep(GetDelay(red));

                // controller.Write(red, LampOff);

                Console.WriteLine("===== Main Menu =====");
                Console.WriteLine();
                Console.WriteLine("0 = Off");
                Console.WriteLine("1 = Red");
                Console.WriteLine("2 = Yellow");
                Console.WriteLine("3 = Green");

                string input = Console.ReadLine();

                switch (input)
                {
                    case "0":
                        TurnOff(controller);
                        break;

                    case "1":
                        TurnOff(controller);
                        controller.Write(red, LampOn);
                        break;

                    case "2":
                        TurnOff(controller);
                        controller.Write(red, LampOn);
                        break;

                    case "3":
                        TurnOff(controller);
                        controller.Write(red, LampOn);
                        break;

                    default:
                        Console.WriteLine("Invalid selection");
                        break;
                }
            }
        }
    }
}
