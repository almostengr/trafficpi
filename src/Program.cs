using System;
using System.Device.Gpio;
using System.Threading;

namespace Almostengr.Rpidotnet
{
    class Program
    {
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
                    min = 1;
                    max = 5;
                    break;
                default:
                    min = 5;
                    max = 10;
                    break;
            }

            return random.Next(min, max) * 1000;
        }

        static void Main(string[] args)
        {
            Console.WriteLine("Traffic light starting...");

            int red = 11;
            int yellow = 9;
            int green = 10;

            using GpioController controller = new GpioController();

            controller.OpenPin(green, PinMode.Output);
            controller.OpenPin(yellow, PinMode.Output);
            controller.OpenPin(red, PinMode.Output);

            Console.CancelKeyPress += (s, e) =>
            {
                Console.WriteLine("Shutting down");
                controller.Write(green, PinValue.High);
                controller.Write(yellow, PinValue.High);
                controller.Write(red, PinValue.High);
            };

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
                Console.WriteLine("high");
            }
        }
    }
}
