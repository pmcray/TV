outputtemplate := "%j.mps";

beginfig(1);
    % Homage to Constantin Brancusi's "Symbol of James Joyce"
    % Consisting of a clockwise spiral, three undulant vertical lines on the right, and a dot.

    % 1. The Clockwise Spiral
    numeric r, k;
    % 3 full revolutions = 1080 degrees. Max radius = 80pt.
    k := 80 / 1080;
    
    path spiral;
    spiral = (0, 0)
    for theta = 5 step 5 until 1080:
        .. ( (theta * k) * sind(theta), (theta * k) * cosd(theta) )
    endfor;
    
    % 2. The Three Undulant Vertical Lines on the right
    path lineA, lineB, lineC;
    lineA = (90, -70) .. (88, -35) .. (91, 0) .. (89, 35) .. (90, 70);
    lineB = (110, -50) .. (112, -15) .. (108, 15) .. (110, 50);
    lineC = (130, -80) .. (128, -40) .. (132, 10) .. (129, 45) .. (130, 80);
    
    % 3. The Dot (shifted from center)
    pair dot_pos;
    dot_pos := (-30, 40);
    
    % 4. Calligraphic Drawing Pen
    pen brush;
    brush := pencircle xscaled 3.5pt yscaled 1.2pt rotated 45;
    
    pickup brush;
    draw spiral;
    draw lineA;
    draw lineB;
    draw lineC;
    
    fill fullcircle scaled 8pt shifted dot_pos;

endfig;
end
