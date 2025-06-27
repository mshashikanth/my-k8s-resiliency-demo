# Use the official Nginx base image
FROM nginx:latest

# --- DEBUGGING STEP: Show content of local index.html before copy ---
# This assumes the Docker build context is the frontend-app directory.
RUN ls -l ./index.html
RUN cat ./index.html

# Copy the custom index.html file
COPY index.html /usr/share/nginx/html/index.html

# --- DEBUGGING STEP: Show content of index.html inside the image after copy ---
RUN ls -l /usr/share/nginx/html/index.html
RUN cat /usr/share/nginx/html/index.html

# Copy the custom nginx.conf file
COPY nginx.conf /etc/nginx/nginx.conf

# --- DEBUGGING STEP: Show content of nginx.conf inside the image after copy ---
RUN ls -l /etc/nginx/nginx.conf
RUN cat /etc/nginx/nginx.conf

# Expose port 80 (default for Nginx)
EXPOSE 80

# Nginx runs as the default command in the base image