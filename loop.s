const const_a (365, 400);
const const_b 1.0, 0.5;
# its ok
loop 1;
	mov
		(365, 400),
		(275, 500),
		$const_b; # its ok
	click left;
	del 20;
	type "hello world";
	loop 2;
		mov $const_a,
			(275, 500),
			4.0, 0.5;
		click right;
		rstr (10, 10);
	end;
end;