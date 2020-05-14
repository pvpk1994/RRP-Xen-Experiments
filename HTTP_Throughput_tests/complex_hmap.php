<?php
    // HTTP Server-Side Program - Final Version
    // Last Updated - May 4, 2020
    // Author:: Pavan Kumar Paluri
    // Copyright @ RT-LAB, University of Houston, 2020
    // 2D associative hash-maps
    
    // NOTE: disable comments // or /* */ to enable print statements
    // Update: Maintain a hash-map for file_size request and directory to choose...
    
    $file_size_requested = ($_GET['random_request']);
    /*
    echo (intval($file_size_requested));
    echo "</br>";
    echo "</br>";
    */
    $num_of_dirs = 3; // Number of sub-directories
    // Change directory to tmpfs now
    chdir('tmpfs');
    // Deploy a switch case for Directory Navigation
    switch ($file_size_requested) {
        case 1000: //1KB
            chdir('one_kb');
            break;
        
        case 100000: //100KB
            chdir('hun_kb');
            break;
            
        case 1000000: //1MB
            chdir('one_mb');
            break;
    }
   
    /*
    print "Current Working Directory::" . getcwd();
    echo "</br>";
    */
    // Pick a random number between specified numbers given a directory
    // Random Number choice range for one_kb:: (0,9), one_mb:: (0,2) and hun_kb: (0,4)
    $random_num = -1;
    
    if( $file_size_requested == 1000) {
        //print "In One KB directory";
        $random_num = rand(0, 9);
        //echo "</br>";
        //print " Rand num is $random_num";
    }
    
    else if($file_size_requested == 100000 ) {
        //print "In Hundred KB Directory";
        $random_num = rand(0, 4);
    }
    
    else if($file_size_requested == 1000000 ) {
        //print "In 1MB directory";
        $radnom_num = rand(0, 2);
    }
    
    if($random_num >= 0)
    {
        $rand_file = $random_num.".txt";
        //echo "</br>";
        //print "Randomly Selected file:: $rand_file";
        //echo "</br>";
    }

    $txt_open = fopen($rand_file, 'r');
    while($line = fgets($txt_open)) {
        echo "</br>";
        echo($line);
    }
    fclose($txt_open);
    ?>
