from sklearn.metrics import f1_score


def macro_f1(y_true, y_pred):
    """Compute macro averaged F1 score."""
    return f1_score(y_true, y_pred, average="macro")
