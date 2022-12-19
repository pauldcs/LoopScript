const APPLY (1175, 1230), (730, 740), 0.1;
const CLAIM (1225, 1275), (773, 780), 0.1;

loop 1000;
	mov $APPLY;
	click left;
	mov $CLAIM;
	click left;
end; 
