{% load staticfiles %}
<!DOCTYPE html>
<html lang="en">
    <head>
      <meta charset="utf-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">
      <link href='https://fonts.googleapis.com/css?family=Petit+Formal+Script' rel='stylesheet' type='text/css'>
      <link rel="stylesheet" href={% static "css/custom.css" %}>
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.2/jquery.min.js"></script>
      <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js" integrity="sha384-0mSbJDEHialfmuBBQP6A4Qrprq5OVfW37PRR3j5ELqxss1yVqOtnepnHVP9aJ7xS" crossorigin="anonymous"></script>
      <title>UNIVISION</title> 
   </head>
    <body>
     <div class="container-fluid">
     <div class="row">
     <div class="col-md-4"></div>
     <div class="col-md-4">
      <div class="contain">
      <h1 id="title">UNIVISION:</h1>
      <p class="tagline">The premier place to share unicorn sightings and stories online.</p>
        <form action="/" method="post">
         {% csrf_token %}
          {{ form }}
          <input type="submit" value="Sign Up" class="btn btn-default"/>
        </form>
	<div class="row">
	  <p>{{msg}}</p>
	</div>
	</div>
	</div>
       <div class="col-md-4"></div>
      </div>
      </div><!--container-fluid-->
    </body>
</html>
