using Microsoft.EntityFrameworkCore;

namespace Almostengr.TrafficPi.Api.Models
{
    public class TrafficSignalDbContext : DbContext
    {
        public TrafficSignalDbContext(DbContextOptions<TrafficSignalDbContext> options) : base(options)
        {

        }

        public DbSet<SignalProgram> SignalPrograms { get; set; }
    }
}