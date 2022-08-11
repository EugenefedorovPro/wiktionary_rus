#defining basic class Dictionary, where all parsed items wil be stored
class Dictionary:
  def __init__(self, word, pos, forms, senses, sounds, status, word_lowcase, stem,
               grammeme, meanings, accent, ipa, npipa, intipa):
    self.word = word
    self.word_lowcase = word_lowcase
    self.stem = stem
    self.pos = pos
    self.grammeme = grammeme
    self.forms = forms
    self.senses = senses
    self.meanings = meanings
    self.accent = accent
    self.sounds = sounds
    self.status = status
    self.ipa = ipa
    self.npipa = npipa
    self.intipa = intipa