#!/bin/bash

echo "🚀 Deploying BNRA System..."
echo "================================"

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose."
    exit 1
fi

echo "📦 Building Docker images..."
docker-compose -f docker/docker-compose.yml build

echo "🚀 Starting services..."
docker-compose -f docker/docker-compose.yml up -d

echo ""
echo "✅ Deployment complete!"
echo "======================="
echo "Dashboard: http://localhost:8050"
echo "API: http://localhost:5000"
echo "API Health: http://localhost:5000/api/health"
echo ""
echo "📋 Quick commands:"
echo "  Stop services: docker-compose -f docker/docker-compose.yml down"
echo "  View logs: docker-compose -f docker/docker-compose.yml logs"
echo "  Restart: docker-compose -f docker/docker-compose.yml restart"
