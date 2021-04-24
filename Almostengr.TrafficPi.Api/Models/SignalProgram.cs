using System.Diagnostics;

namespace Almostengr.TrafficPi.Api.Models
{
    public class SignalProgram
    {
        public SignalProgram(Process process)
        {
            ProcessId = process.Id;
        }

        public int ProcessId { get; set; }
    }
}