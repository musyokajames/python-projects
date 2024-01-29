uncategorized_notes = [note for note in self.notes if note.category not in self.categories]
        # if uncategorized_notes:
        #     print("UNCATEGORIZED:")
        #     for note in uncategorized_notes:
        #         print(note)