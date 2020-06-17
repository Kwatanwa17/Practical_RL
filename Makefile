
start:
	docker-machine start

stop:
	docker-machine stop

run:
	docker run -it -v /c/Users/keita/Documents/Practical_RL-coursera/:/notebooks -p 8888:8888 justheuristic/practical_rl sh ../run_jupyter.sh
