from memory_profiler import memory_usage

def fit_classifier(data, labels, clf, **kwargs):
    clf.fit(data, labels, **kwargs)
    
def measure_memory(data, labels, clf, **kwargs):
    return memory_usage(
        (fit_classifier, (data, labels, clf), kwargs),
        max_usage=True
    )