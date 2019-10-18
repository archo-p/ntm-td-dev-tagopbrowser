"""
Extension classes enhance TouchDesigner components with python. An
extension is accessed via ext.ExtensionClassName from any operator
within the extended component. If the extension is promoted via its
Promote Extension parameter, all its attributes with capitalized names
can be accessed externally, e.g. op('yourComp').PromotedFunction().

Help: search "Extensions" in wiki
"""

from TDStoreTools import StorageManager
TDF = op.TDModules.mod.TDFunctions

class TagOpBrowserExt:
	"""
	TagOpBrowserExt description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp
		self.opBrowser = self.ownerComp.op('opBrowser')
		self.tagOpFind = self.opBrowser.op('treePanel/opfindScopedTag')

	@property
	def ScopedTag(self):
		return self.ownerComp.par.Scopedtag.eval()

	def ToggleOpScopedTag(self, targOp):
		if self.ScopedTag in targOp.tags:
			targOp.tags.remove(self.ScopedTag)
		else:
			targOp.tags.add(self.ScopedTag)

		self.tagOpFind.par.cookpulse.pulse()