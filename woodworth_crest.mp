% The Visibilities - Master Ledger
% Woodworth University Crest (Bifurcated Tracking / Absolute Symmetry)
% Temporal Coordinate: 1914
% Execution: OpTeX / MetaPost

outputtemplate := "%j.mps";

beginfig(1);

    % --- Expanded Mathematical Parameters ---
    numeric R_out, R_in, R_text, p;
    R_out := 205;        % Maximum outer boundary for breathing room
    R_in := 105;         % Unyielding containment wall
    R_text := 155;       % The invisible orbital track
    p := 4;              % The Brutalist tension scalar 
    numeric text_scale; text_scale := 3.8; 

    % --- Locus Generation Engine ---
    vardef norm_radius(expr theta, R_val) =
        R_val / ( (abs(cosd(theta))**p + abs(sind(theta))**p)**(1/p) )
    enddef;

    path outer_band, inner_band, text_track;
    
    outer_band := for t=0 step 1 until 359:
        (norm_radius(t, R_out) * cosd(t), norm_radius(t, R_out) * sind(t)) ..
    endfor cycle;

    inner_band := for t=0 step 1 until 359:
        (norm_radius(t, R_in) * cosd(t), norm_radius(t, R_in) * sind(t)) ..
    endfor cycle;
    
    text_track := for t=0 step 1 until 359:
        (norm_radius(t, R_text) * cosd(t), norm_radius(t, R_text) * sind(t)) ..
    endfor cycle;

    % Render the massive lithic borders
    draw outer_band withpen pencircle scaled 4bp withcolor black;
    draw inner_band withpen pencircle scaled 4bp withcolor black;

    % --- The Alki Lighthouse Schematic ---
    path base, tower, lantern;
    
    base := (-25, -35) -- (25, -35) -- (20, -10) -- (-20, -10) -- cycle;
    tower := (-16, -10) -- (16, -10) -- (10, 45) -- (-10, 45) -- cycle;
    lantern := (-12, 45) -- (12, 45) -- (12, 60) -- (0, 75) -- (-12, 60) -- cycle;
    
    fill base withcolor black;
    fill tower withcolor black;
    fill lantern withcolor black;

    % --- The Asymmetric Projective Beams ---
    path beam_left, beam_right;
    picture light_projection;
    pair focal_point;
    focal_point := (0, 52.5); 
    
    beam_left := focal_point -- (-220, 160) -- (-220, -60) -- cycle;
    beam_right := focal_point -- (220, 90) -- (220, 20) -- cycle;

    light_projection := image(
        fill beam_left withcolor (0.7, 0.7, 0.7);
        fill beam_right withcolor (0.85, 0.85, 0.85); 
    );

    clip light_projection to inner_band;
    draw light_projection;

    % --- The Internal Motto ---
    label("PLURA QUAM VISA" infont defaultfont scaled 1.5, (0, -65)) withcolor black;

    % --- The Bifurcated Typographical Engine (Upper Arc) ---
    string uni_name;
    % * represents the deep lithic bullet
    uni_name := "ARTHUR*JAMES*WOODWORTH*III*UNIVERSITY";
    
    numeric total_arc_length, s_zenith, span_s, half_span;
    numeric step_left, step_right;
    
    total_arc_length := arclength text_track;
    s_zenith := total_arc_length / 4; % Exact 12 o'clock coordinate
    
    % Allocate exactly 82% of the perimeter to prevent bunching
    span_s := total_arc_length * 0.82; 
    half_span := span_s / 2;
    
    % The Mathematical Correction for the 17 vs 19 Character Imbalance
    % Index 17 is 'W' (the exact center of the text string)
    step_left := half_span / 17;
    step_right := half_span / 19;
    
    for i=0 step 1 until 36:
        string char;
        pair pt, tangent_vec;
        numeric target_s, target_t, tangent_angle, up_angle;
        
        char := substring(i, i+1) of uni_name;
        
        % Calculate the bifurcated distance from the Zenith
        if i < 17:
            % Left Hemisphere (17 tracking steps)
            target_s := s_zenith + ((17 - i) * step_left);
        elseif i > 17:
            % Right Hemisphere (19 tracking steps)
            target_s := s_zenith - ((i - 17) * step_right);
        else:
            % The Zenith ('W')
            target_s := s_zenith;
        fi;
        
        % Handle path wrap-around
        if target_s > total_arc_length: target_s := target_s - total_arc_length; fi;
        if target_s < 0: target_s := target_s + total_arc_length; fi;
        
        target_t := arctime target_s of text_track;
        pt := point target_t of text_track;
        
        tangent_vec := direction target_t of text_track;
        tangent_angle := angle(tangent_vec);
        
        % The Absolute Orthotext Correction
        up_angle := tangent_angle - 180;
        
        if char = "*":
            % The Lithic Interpunct (Bullet)
            fill fullcircle scaled 10bp shifted (-1, 1) rotated up_angle shifted pt withcolor (0.3, 0.3, 0.3);
            fill fullcircle scaled 10bp shifted (0.8, -0.8) rotated up_angle shifted pt withcolor (1, 1, 1);
            fill fullcircle scaled 10bp rotated up_angle shifted pt withcolor (0.1, 0.1, 0.1);
        else:
            picture letter_pic;
            letter_pic := char infont defaultfont scaled text_scale;
            pair c; c := center letter_pic;
            
            picture aligned_char;
            aligned_char := image( draw letter_pic shifted -c; );
            
            draw aligned_char shifted (-1, 1) rotated up_angle shifted pt withcolor (0.3, 0.3, 0.3);
            draw aligned_char shifted (0.8, -0.8) rotated up_angle shifted pt withcolor (1, 1, 1);
            draw aligned_char rotated up_angle shifted pt withcolor (0.1, 0.1, 0.1);
        fi;
    endfor;

    % --- The Compressed Pedestal Engine (Lower Arc) ---
    string year_str;
    year_str := "* 1 9 1 4 *"; 
    
    numeric len_year, step_len_year, bottom_s;
    len_year := length(year_str);
    step_len_year := 12; % Violently compressed spacing
    bottom_s := total_arc_length * 0.75; % The nadir
    
    for i=0 step 1 until len_year-1:
        string char;
        pair pt, tangent_vec;
        numeric target_s, target_t, tangent_angle, up_angle_bottom;
        
        char := substring(i, i+1) of year_str;
        
        target_s := bottom_s + ((i - (len_year - 1) / 2) * step_len_year);
        if target_s > total_arc_length: target_s := target_s - total_arc_length; fi;
        
        if char <> " ":
            target_t := arctime target_s of text_track;
            pt := point target_t of text_track;
            
            tangent_vec := direction target_t of text_track;
            tangent_angle := angle(tangent_vec); 
            
            up_angle_bottom := tangent_angle;
            
            if char = "*":
                fill fullcircle scaled 10bp shifted (-1, 1) rotated up_angle_bottom shifted pt withcolor (0.3, 0.3, 0.3);
                fill fullcircle scaled 10bp shifted (0.8, -0.8) rotated up_angle_bottom shifted pt withcolor (1, 1, 1);
                fill fullcircle scaled 10bp rotated up_angle_bottom shifted pt withcolor (0.1, 0.1, 0.1);
            else:
                picture letter_pic;
                letter_pic := char infont defaultfont scaled text_scale;
                pair c; c := center letter_pic;
                
                picture aligned_char;
                aligned_char := image( draw letter_pic shifted -c; );
                
                draw aligned_char shifted (-1, 1) rotated up_angle_bottom shifted pt withcolor (0.3, 0.3, 0.3);
                draw aligned_char shifted (0.8, -0.8) rotated up_angle_bottom shifted pt withcolor (1, 1, 1);
                draw aligned_char rotated up_angle_bottom shifted pt withcolor (0.1, 0.1, 0.1);
            fi;
        fi;
    endfor;

endfig;
end.
