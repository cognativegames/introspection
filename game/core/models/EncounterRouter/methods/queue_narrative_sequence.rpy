init 20 python:
    def queue_narrative_sequence(self, sequence_id):
        """Queue a specific narrative sequence"""
        sequence = narrative_sequences.get(sequence_id, [])
        self.encounter_queue.extend(sequence)

    EncounterRouter.queue_narrative_sequence = queue_narrative_sequence