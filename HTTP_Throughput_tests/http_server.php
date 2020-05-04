<?php
    // HTTP Server-Side Program - Final Version
    // Last Updated - May 4, 2020
    // Author:: Pavan Kumar Paluri
    // Copyright @ RT-LAB, University of Houston, 2020
    // 2D associative hash-maps
    
    // NOTE: disable comments // or /* */ to enable print statements
    
    $file_size_requested = ($_GET['random_request']);
    /*
    echo (intval($file_size_requested));
    echo "</br>";
    echo "</br>";
    */
    $h_map = array();
      $spec_array = array();
      $counter = 0;
      // Iterate through .txt's in ./tmpfs/
      $txt_files = glob('./tmpfs/*.{txt}', GLOB_BRACE);
      foreach ($txt_files as $txt_file) {
         // echo $txt_file . ' - ' . filesize($txt_file) . ' bytes <br/>';
          // Store it in a Hash-Map
          //$h_map[filesize($txt_file)] = $txt_file;
          $h_map[$counter] = array("file_size" => filesize($txt_file),
                                   "file_name" => $txt_file);
          $counter++;
         // echo "</br>";
      }
      // echo gettype(($h_map[6]["file_size"]));
    // echo "</br>";
    for($i=0; $i<$counter; $i++)
    {
        if(intval($file_size_requested) == $h_map[$i]["file_size"])
        {
           // print_r ($h_map[$i]["file_name"]);
           // echo "</br>";
            // load into the array
            array_push($spec_array, $h_map[$i]["file_name"]);
        }
    }
    
    // Pick a random elem from spec_array
    $rand_index = array_rand($spec_array);
    $rand_file = $spec_array[$rand_index];
    /*
    print "Rnadomly Picked file:: $rand_file";
    echo "</br>";
    echo "</br>";
    echo "</br>";
    echo "</br>";
    */
    $txt_open = fopen($rand_file, 'r');
    while($line = fgets($txt_open)) {
        echo($line);
    }
    fclose($txt_open);
    ?>
