function makeCogentSprites(params)
    ps = params.scaling;
    %Sprite 1: 6 grey boxes
    cgmakesprite(1,640*ps,480*ps,0,0,0)
    cgsetsprite(1)
    cgpencol(.45,.45,.45)
    cgrect(params.coords.x,params.coords.y,params.coords.w,params.coords.h)
    cgsetsprite(0)

    %Sprite 2: white box (current location)
    cgmakesprite(2,40*ps,40*ps,0,0,0)
    cgsetsprite(2)
    cgpencol(1,1,1)
    cgrect(0,0,40*ps,40*ps)
    cgsetsprite(0)

    %Sprite 3: Red box (target location)
    cgmakesprite(3,40*ps,40*ps,0,0,0)
    cgsetsprite(3)
    cgpencol(1,0,0)
    cgrect(0,0,params.coords.w(1),params.coords.h(1))
    cgsetsprite(0)
    
    cgmakesprite(4,100*ps,40*ps,0,0,0)
    cgsetsprite(0)
end