<p align="center"><a href="https://github.com/juancrrn/merlin-mobile" target="_blank"><img src="https://juancrrn.io/img/merlin-github-header-rgb-expanded.svg"></a></p>

## About Merlin Classifier

Merlin Desktop is the Merlin project's desktop application AI-based classifier module.

## General structure

## The dispatcher

See: https://softwareengineering.stackexchange.com/questions/170500/what-is-the-difference-of-delegator-and-dispatcher

> Dispatching is not delegating. Dispatcher is more like an intermediary who relays a request to someone else. For example, to attend the meeting my astute junior colleague may ask a cab company for a pick up and the guy receiving the request may dispatch it to a nearby cab driver. The point here is that dispatcher is only passing along the request.

Dispatcher

- The dispatcher can be considered as a Queue where the events are sent.
- A dispatcher runs on the UI thread and executes events for the UI.
- In windows, UI controls may only be modified by the thread that created them, so any changes to the UI must be done from the UI thread - thus that is one of the critical reasons why operations that modify window elements must be sent to the UI's dispatcher.
- A background thread that calls BeginInvoke on the dispatcher will return immediately even though the dispatcher may not have gotten around to processing. If Invoke had been used instead, the background thread would block until the UI thread completed processing. Note that in Silverlight, there is no Invoke on the Dispatcher and in most cases you probably don't want your background thread blocking while the UI thread is processing work.

## The face detection service

## The face embedding generation service

## The face embedding classification service