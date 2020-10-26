using System;
using System.Device.Gpio;
using System.Threading;

namespace Almostengr.TrafficPi
{
    class Program
    {
        private const int red = 11, yellow = 9, green = 10;

        static int GetDelay(int color)
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

        static void TurnOff(GpioController controller)
        {
            controller.Write(green, PinValue.High);
            controller.Write(yellow, PinValue.High);
            controller.Write(red, PinValue.High);
        }

        static void Main(string[] args)
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
                controller.Write(green, PinValue.Low);
                Console.WriteLine("green");

                Thread.Sleep(GetDelay(green));

                controller.Write(green, PinValue.High);
                controller.Write(yellow, PinValue.Low);
                Console.WriteLine("yellow");

                Thread.Sleep(GetDelay(yellow));

                controller.Write(yellow, PinValue.High);
                controller.Write(red, PinValue.Low);
                Console.WriteLine("red");

                Thread.Sleep(GetDelay(red));

                controller.Write(red, PinValue.High);
            }
        }
    }
}
