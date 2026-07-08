

.PHONY: build-image
build-image:
	docker build --platform linux/amd64 . -t gcr.io/csci-242-hci-jrbangit-501812/csci-242-jrbangit:latest


.PHONY: push-image
push-image:
	docker push --platform linux/amd64 gcr.io/csci-242-hci-jrbangit-501812/csci-242-jrbangit:latest
