from .data_model import _BFDataModel as Model


class _BFLikeInterpreter:
    def __getitem__(self, arg):
        if not isinstance(arg, slice):
            raise TypeError(
                f'BFLikeInterpreter indices must be slices, not {type(arg).__name__}'
            )

        # begin of brace
        if arg == slice(None, ..., None):
            child = _BFLikeInnerInterpreter(parent=self)
            child._op_list.append(
                Model.conditional_skip
            )
            self._op_list.append(child)

            return child

        # end of brace
        if arg == slice(..., None, ...):
            self._op_list.append(
                Model.unconditional_jump
            )
            return self._parent

        # other
        self._op_list.append(
            {
                (None, None, None): Model.print_pointee,
                (None, None,  ...): Model.increment_pointee,
                # (None,  ..., None): begin of brace
                (None,  ...,  ...): Model.increment_pointer,
                ( ..., None, None): Model.decrement_pointee,
                # ( ..., None,  ...): end of brace
                ( ...,  ..., None): Model.decrement_pointer,
                ( ...,  ...,  ...): Model.input_to_pointee,
            }[
                arg.start, arg.stop, arg.step
            ]
        )

        return self


class _BFLikeRootInterpreter(_BFLikeInterpreter):
    def __init__(self):
        self._parent = None
        self._indent_level = 0

        self._model = Model()
        self._op_list = []

    def __call__(self):
        for operation in self._op_list:
            operation(self._model)

        self._op_list = []
        return self


class _BFLikeInnerInterpreter(_BFLikeInterpreter):
    def __init__(self, parent):
        self._parent = parent
        self._indent_level = parent._indent_level + 1

        self._op_list = []

    def __call__(self, model):
        conditional_skip, *op_list, unconditional_jump = self._op_list
        assert conditional_skip is Model.conditional_skip
        assert unconditional_jump is Model.unconditional_jump

        while True:
            if conditional_skip(model):
                return self._parent

            for operation in op_list:
                operation(model)
