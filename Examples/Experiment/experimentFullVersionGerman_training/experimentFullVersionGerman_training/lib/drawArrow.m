function drawArrow(prevState, state, choice, params, doHideScore)
    cgpenwid(3);
    coords_xy(1:4)=(params.arrowCoords{prevState, state}(1:4));

    cgdraw(coords_xy(1),coords_xy(2),coords_xy(3),coords_xy(4)) % Draw the line
    dx = coords_xy(3) - coords_xy(1);
    dy = coords_xy(4) - coords_xy(2);
    ang_line = atand(dx/dy); 

    % correct for negative slopes
    if dx >=0 && dy<0 % Diagonally down to the right, or straight down
        ang_line=ang_line+180;
    elseif dx<0 && dy>=0 % Diagonally up to the left, or straight left
        ang_line=ang_line+360;
    elseif dx<0 && dy<0 % Diagonally down to the left
        ang_line=ang_line+180;
    end
    % size of arrow tip
    h=10;
    % Draw the tip appropriately rotated
    a = [h*sind(ang_line),h*cosd(ang_line)]; 
    b = [h*sind(ang_line+120),h*cosd(ang_line+120)];
    c = [h*sind(ang_line+240),h*cosd(ang_line+240)];
    end_x=coords_xy(3);
    end_y=coords_xy(4);
    rotated_1(1)=a(1)+end_x;
    rotated_1(2)=a(2)+end_y;
    rotated_2(1)=b(1)+end_x;
    rotated_2(2)=b(2)+end_y;
    rotated_3(1)=c(1)+end_x;
    rotated_3(2)=c(2)+end_y;
    endline1=[rotated_1(1),rotated_2(1),rotated_3(1)];
    endline2=[rotated_1(2),rotated_2(2),rotated_3(2)];
    cgpolygon(endline1,endline2);

    % label arrow
    lpt1=(params.arrowCoords{prevState,state}(1)+params.arrowCoords{prevState,state}(3))/2;
    lpt2=(params.arrowCoords{prevState,state}(2)+params.arrowCoords{prevState,state}(4))/2;
    
    if prevState == 1 && state == 2 || prevState == 4 && state == 5 || ...
            prevState == 3 && state == 6 || prevState == 6 && state == 3
        lpt2 = lpt2 + 20*params.scaling;
    elseif prevState == 1 && state == 4 || prevState == 2 && state == 3 || ...
            prevState == 3 && state == 4 || prevState == 5 && state == 1 || ...
            prevState == 5 && state == 6
        lpt1 = lpt1 - 30*params.scaling;
    elseif prevState == 2 && state == 5 || prevState == 4 && state == 2 || ...
            prevState == 6 && state == 1
        lpt1 = lpt1 + 30*params.scaling;
    end
    
    if nargin<5 || ~doHideScore
        cgfont(params.fontFamily, params.fontSizeLarge);
        cgtext(sprintf('%i',params.rMatrix(prevState, choice)),lpt1,lpt2);
    end
end