app/routes.py: Google Maps route.                                                                  from flask import render_template

@app.route('/map')
def map():
    return render_template('index.html')                                                                 app/templates/index.html: Google Maps template.                                             <!DOCTYPE html>
<html>
  <head>
    <title>Google Maps</title>
    <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&callback=initMap" async defer></script>
    <style>
      #map {
        height: 400px;
        width: 100%;
      }
    </style>
  </head>
  <body>
    <h1>Google Maps</h1>
    <div id="map"></div>
    <script>
      function initMap() {
        var uluru = {lat: -25.363, lng: 131.044};
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 4,
          center: uluru
        });
        var marker = new google.maps.Marker({
          position: uluru,
          map: map,
          title: 'Hello World!'
        });
      }
    </script>
  </body>
</html>      
