# Use the official Nginx base image
FROM nginx:latest

# Copy the custom index.html file
COPY index.html /usr/share/nginx/html/index.html

# Copy the custom nginx.conf file
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80 (default for Nginx)
EXPOSE 80

# Nginx runs as the default command in the base image
CMD ["nginx", "-g", "daemon off;"]