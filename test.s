loop 10;
	move
		(540, 240)
		(540, 550)
		(1.0, 1.5);
	click right;
	loop 3;
		click right;
		move
			(100, 200)
			(300, 400)
			(0.5, 1.0);
		click left;
		type "hello world";
	end;
end;