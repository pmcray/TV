% Atomic Razor Press - Printer's Device (Calligraphic Edition)
% Refined for MetaPost compatibility and robust intersections
outputtemplate := "%j.mps";

beginfig(1);
    % ------------------------------------------------------------------
    % 1. Core Typographical Parameters
    % ------------------------------------------------------------------
    numeric h, f, i, k;
    h := 100;     % Cap height (radius of the baseline circle)
    f := 0.1;     % Entropic gap fraction (10% rupture)
    i := f * h;   % Absolute physical gap after one full revolution
    k := i / 360; % Radial expansion per degree of clockwise sweep

    % ------------------------------------------------------------------
    % 2. The Calligraphic Nib (Optical Scaling for Debossing)
    % ------------------------------------------------------------------
    pen razor_nib;
    razor_nib := pencircle xscaled 8pt yscaled 1.5pt rotated 45;

    % ------------------------------------------------------------------
    % 3. The Extended Entropic Spiral Boundary
    % ------------------------------------------------------------------
    path boundary;
    boundary = (0, h)
    for d = 1 step 1 until 405:
        .. ( (h + d*k) * sind(d), (h + d*k) * cosd(d) )
    endfor;

    % ------------------------------------------------------------------
    % 4. The Central Pillar
    % ------------------------------------------------------------------
    pair apex, nadir;
    apex := (0, h);
    nadir := (0, -h - (180*k));
    
    path central_pillar;
    central_pillar = apex -- nadir;

    % ------------------------------------------------------------------
    % 5. The Left Leg of 'A' (8 o'clock Vector)
    % ------------------------------------------------------------------
    pair clockEight;
    clockEight := (-h * (sqrt(3)/2), -h/2);
    
    path ray_A_left;
    % Offset start to avoid immediate intersection at apex
    ray_A_left := (apex + 0.1*(clockEight-apex)) -- (apex + 3 * (clockEight - apex)); 
    
    pair intersect_A;
    intersect_A := ray_A_left intersectionpoint boundary;
    
    path leg_A;
    leg_A := apex -- intersect_A;

    % ------------------------------------------------------------------
    % 6. The Right Leg of 'R' (4:30 Vector)
    % ------------------------------------------------------------------
    pair clockFourThirty;
    clockFourThirty := (h * (sqrt(2)/2), -h * (sqrt(2)/2));
    
    path ray_R_right;
    % Offset start to avoid origin intersection
    ray_R_right := (0.1 * clockFourThirty) -- (3 * clockFourThirty);
    
    pair intersect_R;
    intersect_R := ray_R_right intersectionpoint boundary;
    
    path leg_R;
    leg_R := (0, 0) -- intersect_R;

    % ------------------------------------------------------------------
    % 7. The Clipped Horizontal Crossbar
    % ------------------------------------------------------------------
    pair right_crossbar_node;
    right_crossbar_node := (h + 90*k, 0); 
    
    path ray_horizontal;
    ray_horizontal := (-2h, 0) -- (2h, 0);
    
    pair left_crossbar_node;
    left_crossbar_node := ray_horizontal intersectionpoint leg_A;
    
    path crossbar;
    crossbar := left_crossbar_node -- right_crossbar_node;

    % ------------------------------------------------------------------
    % 8. Rendering Protocol
    % ------------------------------------------------------------------
    pickup razor_nib;
    
    draw boundary;
    draw central_pillar;
    draw leg_A;
    draw leg_R;
    draw crossbar;

endfig;
end
