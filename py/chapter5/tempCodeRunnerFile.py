try:
            for i in range(self._n):
                if self._A[i] is not None:
                    return False
            return True
        except Exception as e:
            print(f"An error occurred: {e}")
            return True