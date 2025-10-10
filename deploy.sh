cd /home/deploy/project/psy_django || exit 1

echo "Pulling latest changes from main..."
git fetch origin main
git reset --hard origin/main

echo "Rebuilding Docker containers..."
docker-compose down
docker-compose up -d --build

echo "Cleaning up unused Docker images..."
docker system prune -af

echo "Deployment finished. Showing container status:"
docker ps